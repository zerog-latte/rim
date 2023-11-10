<template>
  <div>
    <div v-for="(category, key) in data" :key="key">
      <div>
        <div v-if="category.subcats && !category.parent">
          <h3 class="cap">{{ category._id }}</h3>
        </div>
        <div v-else>
          <h5><span class="cap">{{ category._id }}</span> - {{ category.desc }}</h5>
          <ul v-if="category.items">
            <li v-for="(item, index) in category.items" :key="index">
              {{ item.desc }}
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.cap {
  text-transform: capitalize;
}
</style>

<script>
import axios from 'axios';

export default {
  name: 'Getdata',
  data() {
    return {
      data: [],
    };
  },
  methods: {
    getCategories() {
      axios.get('/categories')
        .then((res) => {
          this.data = res.data;
          this.getCategoryContent();
        })
        .catch((error) => {
          console.error(error);
        });
    },
    async getCategoryContent() {
      for (const cat of this.data) {
        await axios
          .get(`/items/${cat._id}`)
          .then((res) => {
            cat.items = res.data;
          })
          .catch((error) => {
            console.error(error);
          });
      }
    },
  },
  created() {
    this.getCategories();
  },
};
</script>