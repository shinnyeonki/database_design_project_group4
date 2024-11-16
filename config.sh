#!/bin/bash

#만약 가상환경이 존재하지 않는다면
if [ ! -d ".venv" ]; then
    # 가상환경 생성
    python -m venv .venv
    echo "가상환경 생성 완료"
fi

# 만약 현제 가상환경이 활성화 되어있지 않다면
if [ -z "$VIRTUAL_ENV" ]; then
    # 가상환경 활성화
    source .venv/bin/activate
    echo "가상환경 활성화 완료"
fi