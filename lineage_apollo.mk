#
# Copyright (C) 2021 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0
#

# Inherit from those products. Most specific first.
$(call inherit-product, $(SRC_TARGET_DIR)/product/core_64_bit.mk)
$(call inherit-product, $(SRC_TARGET_DIR)/product/full_base_telephony.mk)

# Inherit some common Lineage stuff.
$(call inherit-product, vendor/lineage/config/common_full_phone.mk)

# Inherit from apollo device
$(call inherit-product, device/xiaomi/apollo/device.mk)

#Axion Bringup!
TARGET_INCLUDES_LOS_PREBUILTS := true
PRODUCT_NO_CAMERA := false
TARGET_INCLUDE_VIPERFX := true

AXION_CAMERA_REAR_INFO := 64,13,5

AXION_CAMERA_FRONT_INFO := 20

AXION_MAINTAINER := Murtaza_Kolachi

AXION_PROCESSOR := Snapdragon_865_(7nm)

AXION_CPU_PRIME_CORES := 7
AXION_CPU_BIG_CORES := 4,5,6
AXION_CPU_SMALL_CORES := 0,1,2,3

PRODUCT_SYSTEM_PROPERTIES += \
    persist.sys.axion_cpu_prime=$(AXION_CPU_PRIME_CORES) \
    persist.sys.axion_cpu_big=$(AXION_CPU_BIG_CORES) \
    persist.sys.axion_cpu_small=$(AXION_CPU_SMALL_CORES)

# Boot animation
TARGET_BOOT_ANIMATION_RES := 1080

PRODUCT_NAME := lineage_apollo
PRODUCT_DEVICE := apollo
PRODUCT_MANUFACTURER := Xiaomi
PRODUCT_BRAND := Xiaomi
PRODUCT_MODEL := Xiaomi Mi 10T

PRODUCT_GMS_CLIENTID_BASE := android-xiaomi

PRODUCT_BUILD_PROP_OVERRIDES += \
    BuildDesc="apollo_global-user 12 RKQ1.211001.001 V14.0.4.0.SJDMIXM release-keys" \
    BuildFingerprint=Xiaomi/apollo_global/apollo:12/RKQ1.211001.001/V14.0.4.0.SJDMIXM:user/release-keys
