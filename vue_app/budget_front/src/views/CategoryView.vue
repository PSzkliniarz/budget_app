<template>
  <div style="background-color: #E3E3E3">
    <CategoriesTable/>
  </div>
</template>

<script>

  import CategoriesTable from "@/components/CategoriesTable";

  export default {
    name: 'Category_View',

    components: {
      CategoriesTable
    },
  }
</script>
