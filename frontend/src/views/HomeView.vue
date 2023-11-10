<template>
  <div class="home">
    <div class="logo">
    <img alt="Vue logo" src="../assets/rim.png">
    </div>
    <Main msg="Welcome to Your Vue.js App"/>
  </div>
</template>

<script>
// @ is an alias to /src
import Main from '@/components/Main.vue'

export default {
  name: 'HomeView',
  components: {
    Main
  }
}
</script>
