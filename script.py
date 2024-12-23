name: "send email after workflow"

on:
    workflow_dispatch:

jobs:
    send_email:
        runs-on: ubuntu-latest
        steps:
            - name: "checkout code"
              uses: action/checkout@v2

            - name: "setup python env"
              uses: action/setup-python@v2
              with:
                  python-version: '3.x'

            - name: "install  dependencies"
              run: |
                python -m pip install --upgrade pip
            

            - name: "send mail by executing python script"
              run: python script.py 
              env:
                WORKFLOW_NAME: ${{ github.workflow }}
                REPO_NAME: ${{ github.repository }}
                SENDER_PASSWORD: ${{ secrets.SENDER_PASSWORD }}
                SENDER_EMAIL: ${{ secrets.SENDER_EMAIL }}
                RECEIVER_EMAIL: ${{ secrets.RECEIVER_EMAIL }}
