/*
 * SPDX-FileCopyrightText: (C) 2025 Paranoid Android
 * SPDX-License-Identifier: Apache-2.0
 */

#define LOG_TAG "CameraProviderExtension"

#include "CameraProviderExtension.h"
#include <android-base/file.h>
#include <android-base/logging.h>

using ::android::base::ReadFileToString;
using ::android::base::WriteStringToFile;

static const std::string kToggleSwitch = "/sys/class/leds/led:switch_0/brightness";
static const std::string kTorchBrightnessNodes[] = {
    "/sys/class/leds/led:torch_0/brightness",
    "/sys/class/leds/led:torch_1/brightness"
};

bool supportsTorchStrengthControlExt() {
    return true;
}

bool supportsSetTorchModeExt() {
    return false;
}

int32_t getTorchDefaultStrengthLevelExt() {
    return 80;
}

int32_t getTorchMaxStrengthLevelExt() {
    // Hardware limit is 500, however we limit to 200 for safety reasons.
    return 200;
}

int32_t getTorchStrengthLevelExt() {
    // We write the same value in all the LEDs, so get from the first one.
    auto node = kTorchBrightnessNodes[0];
    if (std::string value; ReadFileToString(node, &value, true))
        return std::stoi(value);
    else
        LOG(ERROR) << "Failed to read from node: " << node;

    return getTorchDefaultStrengthLevelExt();
}

void setTorchStrengthLevelExt(int32_t torchStrength, bool enabled) {
    WriteStringToFile("0", kToggleSwitch, true);
    LOG(DEBUG) << "setTorchStrengthLevelExt(" << torchStrength << ")";
    auto value = std::to_string(torchStrength);
    for (auto& node : kTorchBrightnessNodes) {
        if (!WriteStringToFile(value, node, true))
            LOG(ERROR) << "Failed writing value " << value << " to node: " << node;
    }
    if (enabled) {
        WriteStringToFile("255", kToggleSwitch, true);
    }
}

void setTorchModeExt(bool enabled) {
    int32_t strength = getTorchDefaultStrengthLevelExt();
    setTorchStrengthLevelExt(enabled ? strength : 0, enabled);
}
