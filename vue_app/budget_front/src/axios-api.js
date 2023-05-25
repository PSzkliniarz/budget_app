import axios from "axios";
import store from "@/store"; // Importuj instancję Vuex store

const axiosInstance = axios.create({
  baseURL: 'http://127.0.0.1:8000',
  timeout: 1000,
  headers: {
    Authorization: `Bearer`
  }
});

axiosInstance.interceptors.request.use(
  function (config) {
    // Dodaj nagłówek Authorization do żądania
    config.headers.Authorization = `Bearer ${store.state.accessToken}`;
    return config;
  },
  function (error) {
    return Promise.reject(error);
  }
);

export default axiosInstance;
