# First stage: Inherit from Python image
FROM python:3.10-alpine AS builder

# Set the working directory
WORKDIR /app

# Copy the application code
COPY . .

# Run the build script
RUN python build.py

# Second stage: Inherit from Node.js image
FROM node:20-alpine AS node_builder

# Install git
RUN apk add --no-cache git

# Set the working directory
WORKDIR /app

# Copy the content from the first stage
COPY --from=builder /app /app

# Install Node.js dependencies
RUN npm install --no-cache

# Build the VitePress site
RUN npm run docs:build

# Third stage: Inherit from Nginx image
FROM nginx:alpine

# Copy the built site from the second stage
COPY --from=node_builder /app/.vitepress/dist /usr/share/nginx/html

# Copy the Nginx configuration file
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Expose the port the app runs on
EXPOSE 8080

# Command to run Nginx
CMD ["nginx", "-g", "daemon off;"]