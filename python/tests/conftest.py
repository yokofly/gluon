"""
conftest.py
"""
import pytest
import os

from timeplus import Env


@pytest.fixture
def staging_environment():
    token = os.environ.get("AUTH0_API_TOKEN")
    env = (
        Env().schema("https").host("staging.demo.timeplus.io").port("443").token(token)
    )
    # set current environment when you have more than 1 environment
    Env.setCurrent(env)
    return env


@pytest.fixture
def demo_environment():
    token = os.environ.get("AUTH0_API_TOKEN")
    env = Env().schema("https").host("demo.timeplus.com").port("443").token(token)
    Env.setCurrent(env)
    return env


@pytest.fixture
def playground_environment():
    env = Env().schema("https").host("play.timeplus.com").port("443")
    Env.setCurrent(env)
    return env


@pytest.fixture
def local_environment():
    env = Env()
    Env.setCurrent(env)
    return env
