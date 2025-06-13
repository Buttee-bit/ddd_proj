# Stage 1: Build Vue app
FROM node:22.16.0-slim AS build-stage

RUN corepack enable && corepack prepare pnpm@latest --activate

WORKDIR /app

COPY client/package*.json ./
COPY client/pnpm-lock.yaml ./

RUN pnpm install --frozen-lockfile

COPY client/ .
RUN pnpm run build-only

FROM nginx:stable-alpine AS production-stage
COPY client/dist ./etc/nginx/main/
COPY nginx/default.conf ./etc/nginx/conf.d/default.conf

CMD ["nginx", "-g", "daemon off;"]