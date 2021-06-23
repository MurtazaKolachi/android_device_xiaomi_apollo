/*
 * Copyright (C) 2021 The LineageOS Project
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#include <string>

typedef struct variant_info {
    std::string sku_value;

    std::string brand;
    std::string device;
    std::string model;
    std::string build_description;
    std::string build_fingerprint;
} variant_info_t;

void search_variant(const variant_info_t variants[]);
void set_variant_props(const variant_info_t variant);

void property_override(char const prop[], char const value[], bool add = true);
void set_ro_build_prop(const std::string &prop, const std::string &value, bool product = false);
