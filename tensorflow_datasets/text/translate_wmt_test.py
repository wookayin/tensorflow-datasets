# coding=utf-8
# Copyright 2018 The TensorFlow Datasets Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Tests for WMT translate dataset module."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow_datasets.testing import dataset_builder_testing
from tensorflow_datasets.text import translate_wmt


class TranslateWMTTest(dataset_builder_testing.TestCase):
  DATASET_CLASS = translate_wmt.TranslateWmt
  BUILDER_CONFIG_NAMES_TO_TEST = ["ende_plain_text_t2t", "ende_subwords8k_t2t"]

  DL_EXTRACT_RESULT = {
      "train_0": "nc_v13",
      "train_1": "crawl",
      "train_2": "europarl",
      "test_0": "task",
  }

  SPLITS = {
      "train": 5,
      "test": 2,
  }


if __name__ == "__main__":
  dataset_builder_testing.main()
