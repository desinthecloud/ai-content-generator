AI Content Generator with Bedrock

This project uses Amazon Bedrock + Claude 2.1 to generate high-quality AI content via a Lambda backend and Streamlit frontend.

Features
Claude 2.1 prompt handling
API Gateway (HTTP API) integration
Streamlit frontend UI
AWS Lambda backend
Fully serverless and low-cost

Tech Stack
Amazon Bedrock (Claude v2.1)
AWS Lambda
API Gateway (HTTP)
IAM
Streamlit
Python 3.11

Setup Instructions
Full setup instructions are available in the /docs/Instructions_Notion.md.

Shutdown Checklist
To avoid ongoing AWS charges:
- ❌ Delete API Gateway
- ❌ Delete CloudWatch log group for the Lambda
- ❌ (Optional) Delete the Lambda function
- ✅ Just stop calling Claude via Bedrock — no usage = no charge
  
See /docs/Shutdown_Notion.md for full cleanup steps.

👩🏾‍💻 Created by Desiree’ Weston
Follow the journey at desinthecloud.com
