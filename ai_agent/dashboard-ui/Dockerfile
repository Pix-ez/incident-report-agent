# --- STAGE 1: Build the Application ---
FROM node:20-alpine AS builder
WORKDIR /app

# Copy package files first to leverage Docker layer caching
COPY package.json package-lock.json ./

# Install dependencies using clean install (ignores devDependencies if needed, but Vite requires them to build)
RUN npm install

# Copy the rest of the source code
COPY . .

# Build the production assets (outputs to /app/dist)
RUN npm run build

# --- STAGE 2: Serve with Production-Ready Nginx ---
FROM nginx:1.25-alpine AS runner
WORKDIR /usr/share/nginx/html

# Clean the default public directory
RUN rm -rf ./*

# Copy built static files from the builder stage
COPY --from=builder /app/dist .

# Copy custom Nginx configuration for SPA routing and compression
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
