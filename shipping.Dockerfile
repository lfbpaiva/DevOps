FROM node:22-alpine
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci --omit=dev
COPY proto/shipping.proto ./proto/shipping.proto
COPY services/shipping/index.js ./services/shipping/index.js
COPY LICENSE ./LICENSE
CMD ["node", "/app/services/shipping/index.js"]
