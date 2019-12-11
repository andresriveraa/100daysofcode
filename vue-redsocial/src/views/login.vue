<template>
  <div class="maincontentlogin">
    <!-- logo -->
    <div class="logoredsocial">
      <figure>
        <img class="logologin" src="@/assets/logo.png" alt="">
      </figure>
    </div>
    <!-- form -->
    <div class="formDataUser">
      <div class="contentLogin">
        <div class="username">
          <input v-model="user" placeholder="Username" type="text" id="username">
        </div>
        <div class="password">
          <input type="text" id="password" placeholder="Contraseño">
        </div>
      </div>
      <div class="buttonContent">
        <div class="btn">Send email
        </div>
      </div>
    </div>
    <!-- endform -->
  </div>
</template>

<script>
import { mapState } from 'vuex';

export default {
  data() {
    return {
      user: '',
    };
  },
  computed: {
    ...mapState([
      'userV',
    ]),
  },

};

</script>

<style>
@import '../assets/statics/login.css';
</style>
