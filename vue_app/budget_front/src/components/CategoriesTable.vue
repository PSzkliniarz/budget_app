<template>
  <div>
    <h1>Kategorie</h1>
    <v-data-table
        :headers="headers"
        :items="getCategories || []"
        :items-per-page="5"
        class="elevation-1"
        :search="search"
    >
      <template v-slot:top>
        <v-text-field
            v-model="search"
            label="Szukaj kategori"
            class="mx-4"
        ></v-text-field>
      </template>
      <template v-slot:[`item.title`]="{ item }">
        {{ capitalize(item.name) }}
      </template>
    </v-data-table>
  </div>
</template>

<script>
import {mapActions, mapGetters} from "vuex";

export default {
  name: "CategoriesTable",
  data() {
    return {
      search: '',
    }
  },
  computed: {
    ...mapGetters(['getCategories']),
    headers() {
      return [
        {text: 'Nazwa', value: 'name'},
      ]
    },
  },
  methods: {
    ...mapActions(['loadCategories']),
    capitalize(str) {
      return str[0].toUpperCase() + str.slice(1);
    }
  },
  created() {
    this.loadCategories();
  },
}
</script>

<style scoped>

</style>