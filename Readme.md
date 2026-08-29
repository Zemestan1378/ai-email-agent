# AI Email Agent

A local AI-powered email assistant built with Python, Ollama, Qwen, and RAG.

## Overview

This project is an experimental AI Agent for managing and understanding emails using local Large Language Models.

The goal is to build an agent that can:

- Understand user requests
- Search emails
- Retrieve specific emails
- Perform semantic search using RAG
- Use tools autonomously
- Generate reply drafts
- Keep humans in the loop before sensitive actions

## Current Architecture

```text
User
  ↓
AI Agent
  ↓
Local LLM (Qwen via Ollama)
  ↓
Tool Decision
  ↓
Tool Dispatcher
  ├── Keyword Email Search
  ├── Semantic Search / RAG
  ├── Get Email
  └── Draft Reply
  ↓
Tool Result
  ↓
AI Agent
  ↓
Final Response