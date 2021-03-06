#!/usr/bin/env python
"""Tests for `tekton-neat` package."""
import yaml

from tekton_neat.tekton_neat import process

sample_document = """
---
  metadata:
    managedFields:
      foo: 1
"""


def test_content():
    ret = yaml.safe_load("\n".join(process(sample_document)))
    assert 'managedFields' not in ret['metadata']
