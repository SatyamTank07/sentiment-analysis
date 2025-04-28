# Step 1: Build
FROM node:18 AS build

WORKDIR /app

# Copy package files first (better layer caching)
COPY package*.json ./

# Install dependencies - using standard install instead of ci due to rollup issues
RUN npm install

# Copy source files
COPY . .

# Build the application
RUN npm run build

# Step 2: Serve
# Step 2: Serve
FROM nginx:alpine

# Copy built files
COPY --from=build /app/dist /usr/share/nginx/html

# Copy custom nginx config
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Healthcheck
HEALTHCHECK --interval=30s --timeout=3s CMD wget -q -O - http://localhost:3000/ || exit 1

EXPOSE 3000

CMD ["nginx", "-g", "daemon off;"]
