import axios from "axios";

const api = axios.create({ baseURL: "https://fakestoreapi.com" });
// http://192.168.20.27:8000/api/v1/rest/chat
api.interceptors.response.use(
  (response) => response.data,
  (error) => Promise.reject(error)
);

export default api;
