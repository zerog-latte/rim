<template>
<table align="center" width="90%">
  <tr>
    <th>#</th><th>id</th><th>parent</th><th>description</th><th>children</th>
  </tr>
  <tr v-for="(item, key) in data" :key="key">
  <th>{{key}}</th>
  <td>{{ item._id }}</td>
  <td>{{ item.parent }}</td>
  <td>{{ item.desc }}</td>
  <td>
    <small>
      <span v-for="(v, k) in item.subcats" :key="k">{{v}}, </span>
    </small>
  </td>
  </tr>
</table>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Ping',
  data() {
    return {
      data: [],
    };
  },
  methods: {
    getMessage() {
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
    this.getMessage();
  },
};
</script>