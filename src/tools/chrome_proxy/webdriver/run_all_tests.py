# Copyright 2016 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import common
import sys

if __name__ == "__main__":
  results = common.IntegrationTest.RunAllTests(run_all_tests=True)
  if results.errors or results.failures:
    sys.exit(2)
