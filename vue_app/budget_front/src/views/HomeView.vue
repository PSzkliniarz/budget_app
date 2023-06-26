<template>
  <div style="background-color: #E3E3E3">
    <DoughnutChart />
    <ExpenseTable/>
  </div>
</template>

<script>
  import DoughnutChart from "@/components/DoughnutChart";
  import ExpenseTable from "@/components/ExpenseTable";

  export default {
    name: 'Home_default',

    components: {
      DoughnutChart,
      ExpenseTable,
    },
  }
</script>
