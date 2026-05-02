import axios from "axios";

const request = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL,
  timeout: 12000
});

request.interceptors.request.use((config) => {
  return config;
});

request.interceptors.response.use((response) => response);

export default request;
