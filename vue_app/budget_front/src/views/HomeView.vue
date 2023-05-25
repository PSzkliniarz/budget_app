<template>
  <div>
    <AccountsTest/>
    <ExpenseTable/>
  </div>
</template>

<script>
  import AccountsTest from "@/components/Accounts";
  import ExpenseTable from "@/components/ExpenseTable";

  export default {
    name: 'Home_default',

    components: {
      ExpenseTable,
      AccountsTest,
    },
  }
</script>
