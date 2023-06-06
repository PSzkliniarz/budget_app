<template>
  <div class="chart-container">
    <h2>test</h2>
    {{ filteredExpenses }}
    <div class="filter-container">
      <v-select v-model="selectedPeriod" :items="periodOptions" label="Select Period" @change="filterExpenses "/>
    </div>
    <Doughnut :data="chartData" :options="chartOptions"/>
  </div>
</template>

<script>
import {Doughnut} from 'vue-chartjs';
import {Chart as ChartJS, Title, Tooltip, Legend, ArcElement, CategoryScale, LinearScale} from 'chart.js';
import {mapGetters} from 'vuex';

ChartJS.register(Title, Tooltip, Legend, ArcElement, CategoryScale, LinearScale);

export default {
  name: 'DoughnutChart',
  components: {Doughnut},

  computed: {
    ...mapGetters(['getExpenses']),

    chartData() {
      const categoryData = this.getCategoryData();
      return {
        labels: categoryData.labels,
        datasets: [
          {
            label: 'Amount',
            backgroundColor: categoryData.colors,
            data: categoryData.amounts,
          },
        ],
      };
    },

    chartOptions() {
      return {
        responsive: true,
      };
    },
    periodOptions() {
      return ['Current Month', 'Current Week'];
    },
  },
  data() {
    return {
      selectedPeriod: 'Current Month',
      filteredExpenses: [],
    };
  },

  methods: {
    getCategoryData() {
      const categories = {};
      const labels = [];
      const amounts = [];
      const colors = [];

      for (const expense of this.filteredExpenses) {
        const categoryName = expense.category_name;
        const amount = expense.amount;

        if (!categories[categoryName]) {
          categories[categoryName] = 0;
        }

        categories[categoryName] += amount;
      }

      for (const category in categories) {
        labels.push(category);
        amounts.push(categories[category]);
        colors.push(getRandomColor());
      }

      return {
        labels,
        amounts,
        colors,
      };
    },
    filterExpenses() {
      if (Array.isArray(this.getExpenses)) {
        const currentDate = new Date();

        if (this.selectedPeriod === 'Current Month') {
          const currentMonth = currentDate.getMonth() + 1;
          const currentYear = currentDate.getFullYear();
          this.filteredExpenses = this.getExpenses.filter((expense) => {
            const expenseDate = new Date(expense.data);
            const expenseMonth = expenseDate.getMonth() + 1;
            const expenseYear = expenseDate.getFullYear();
            return expenseMonth === currentMonth && expenseYear === currentYear;
          });
        } else if (this.selectedPeriod === 'Current Week') {
          const currentDay = currentDate.getDate();
          const currentWeekStart = currentDay - currentDate.getDay();
          const currentWeekEnd = currentWeekStart + 6;
          this.filteredExpenses = this.getExpenses.filter((expense) => {
            const expenseDate = new Date(expense.data);
            const expenseDay = expenseDate.getDate();
            return expenseDay >= currentWeekStart && expenseDay <= currentWeekEnd;
          });
        }
      } else {
        this.filteredExpenses = [];
      }
    },

  },
  watch: {
    getExpenses(newExpenses) {
      if (newExpenses.length > 0) {
        this.filterExpenses();
      }
    },
  },
};

function getRandomColor() {
  const letters = '0123456789ABCDEF';
  let color = '#';
  for (let i = 0; i < 6; i++) {
    color += letters[Math.floor(Math.random() * 16)];
  }
  return color;
}
</script>

<style>
.chart-container {
  width: 100%;
  height: 500px;
  display: flex;
  justify-content: center;
}
</style>
