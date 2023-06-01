<template>
  <div>
    <AccountsTest/>
    <DoughnutChart />
    <ExpenseTable/>
  </div>
</template>

<script>
  import AccountsTest from "@/components/Accounts";
  import DoughnutChart from "@/components/DoughnutChart";
  import ExpenseTable from "@/components/ExpenseTable";

  export default {
    name: 'Home_default',

    components: {
      DoughnutChart,
      ExpenseTable,
      AccountsTest,
    },
  }
</script>
