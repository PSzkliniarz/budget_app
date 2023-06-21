import axios from "axios";
import store from "@/store"; // Importuj instancję Vuex store

const axiosInstance = axios.create({
  baseURL: 'http://127.0.0.1:8000',
  timeout: 1000,
});

axiosInstance.interceptors.request.use(
  function (config) {
    // Sprawdź, czy użytkownik jest zalogowany
    if (store.state.accessToken) {
      // Jeśli token dostępu jest dostępny, dodaj nagłówek Authorization
      config.headers.Authorization = `Bearer ${store.state.accessToken}`;
    }
    return config;
  },
  function (error) {
    return Promise.reject(error);
  }
);

export default axiosInstance;
