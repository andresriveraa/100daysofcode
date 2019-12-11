<template>
  <div id="app">
    <div id="nav">
      <!-- <router-link to="/">Home</router-link> | -->
      <!-- <router-link to="/about">About</router-link> -->
      <loginPm />
    </div>
    <router-view/>
  </div>
</template>

<script>
import loginPm from '@/views/login.vue';

export default {
  components: {
    loginPm,
  },
};
</script>
