#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)
from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.fixups_lib import (
    lib_fixups,
    lib_fixups_user_type,
)

# Define all blob-specific binary fixups
blob_fixups: blob_fixups_user_type = {
    'vendor/etc/libnfc-nci.conf': blob_fixup()
        .add_line_if_missing('# Mifare Tag implementation\n# 0: General implementation\n# 1: Legacy implementation\nLEGACY_MIFARE_READER=1'),
    'vendor/lib64/camera/components/com.mi.node.watermark.so': blob_fixup()
        .add_needed('libpiex_shim.so'),
    'vendor/lib64/libril-qc-hal-qmi.so': blob_fixup()
        .binary_regex_replace(b'ro.product.vendor.device', b'ro.vendor.radio.midevice'),
    'vendor/lib64/vendor.qti.hardware.camera.postproc@1.0-service-impl.so': blob_fixup()
        .binary_regex_replace(b'\x9A\x0A\x00\x94', b'\x1F\x20\x03\xD5'),
    'vendor/etc/init/init.mi_thermald.rc': blob_fixup()
        .regex_replace('.*seclabel u:r:mi_thermald:s0\n', ''),
    'vendor/etc/init/init.batterysecret.rc': blob_fixup()
        .regex_replace('.*seclabel u:r:batterysecret:s0\n', ''),
    'vendor/etc/init/init_thermal-engine.rc': blob_fixup()
        .uncomment_lines_between(r'^#service', r'^$'),
    'vendor/lib64/libdlbdsservice.so': blob_fixup()
        .replace_needed("libstagefright_foundation.so", "libstagefright_foundation-v33.so"),
    'vendor/lib/libstagefright_soft_ac4dec.so': blob_fixup()
        .replace_needed("libstagefright_foundation.so", "libstagefright_foundation-v33.so"),
    'vendor/lib/libstagefright_soft_ddpdec.so': blob_fixup()
        .replace_needed("libstagefright_foundation.so", "libstagefright_foundation-v33.so"),
    'vendor/lib64/libarcsoft_single_chart_calibration.so': blob_fixup()
        .replace_needed("libstdc++.so", "libstdc++_vendor.so"),
    'vendor/etc/seccomp_policy/atfwd@2.0.policy': blob_fixup()
        .add_line_if_missing('gettid: 1'),
    'vendor/lib64/libwvhidl.so': blob_fixup()
        .add_needed('libcrypto_shim.so'),
    'vendor/lib64/mediadrm/libwvdrmengine.so': blob_fixup()
        .add_needed('libcrypto_shim.so'),
}  # fmt: skip

# You can customize lib fixups here if needed
lib_fixups: lib_fixups_user_type = {
    **lib_fixups,
}

# Required namespaces to avoid Soong build errors
namespace_imports = [
    'device/xiaomi/apollo',
    'hardware/qcom-caf/sm8250/audio',
    'hardware/qcom-caf/sm8250/display',
    'hardware/qcom-caf/sm8250/media',
    'hardware/xiaomi',
    'vendor/qcom/opensource/commonsys-intf/display',
    'vendor/qcom/opensource/commonsys/display',
    'vendor/qcom/opensource/dataservices',
    'vendor/qcom/opensource/display',
    'vendor/xiaomi',
]

# Main module config
module = ExtractUtilsModule(
    'apollo',
    'xiaomi',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
)

# Entrypoint
if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()
