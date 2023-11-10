<template>
<div>
  <div v-for="(category, key) in data" :key="key">
    <div>
      <div v-if="category.subcats && !category.parent">
        <h3 class="cap">{{category._id}}</h3>
      </div>
      <div v-else>
        <span class="cap">{{category._id}}</span> - {{category.desc}}
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
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
  created() {
    this.getCategories();
  },
};
</script>