FROM node

WORKDIR /app

COPY ./app .

RUN npm install

EXPOSE 5173

CMD ["sh", "-c", "echo \"VITE_URL_BASE=$URL_BASE\" > .env && npm run dev -- --host 0.0.0.0"]
#CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]







