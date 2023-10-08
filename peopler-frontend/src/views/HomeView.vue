<template>
  <div id='bg'></div>
  <div class="home">
    <h1>Peopler</h1>
    <h2>Get to know your community</h2>
    <TransitionGroup>
      <div v-if='step === 1'>
        <input @keyup.enter='cont' v-model='email_val' placeholder='Enter your email to get started...'/><button v-if='!showSpin' @click='cont'><fa-icon icon='fas fa-fw fa-arrow-right'></fa-icon></button><button v-else><fa-icon icon='fas fa-fw fa-circle-notch' spin></fa-icon></button>
      </div>
      <div v-if='step === 2'>
        <p>A six-digit code has been emailed to <b>{{ email_val }}</b>. <br/>Please enter the code you received to finish signing in.</p>
        <input maxlength='6' v-model='code_val' @keyup.enter='cont2' placeholder='Confirmation Code'/><button v-if='!showSpin' @click='cont2'><fa-icon icon='fas fa-fw fa-arrow-right'></fa-icon></button><button v-else><fa-icon icon='fas fa-fw fa-circle-notch' spin></fa-icon></button>
      </div>
    </TransitionGroup>
  </div>
</template>

<style scoped>
  #bg {
    position: fixed;
    background-image: url('../assets/landingbg.jpg');
    background-position: center;
    background-size: cover;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: -1;
    opacity: 0.7;
  }

  .home {
    margin-left: 5vw;
    margin-top: 15vh;
  }

  h1 {
    font-size: 60px;
    margin: 0;
  }

  h2 {
    font-size: 30px;
    margin: 0;
    font-weight: 500;
    margin-bottom: 60px;
  }

  p {
    margin-top: 0;
  }

  input {
    width: 400px;
    /* border-top-right-radius: 0;
    border-bottom-right-radius: 0; */
    /* border-right: none; */
  }
  button {
    width: 40px;
    overflow: hidden;
    margin-left: -41px;
    border-top-left-radius: 0;
    border-bottom-left-radius: 0;
    border: none;
    border-left: 1px solid #0000004f;
    background-color: none;
  }
</style>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'HomeView',
  components: {
    // HelloWorld
  },
  data: function () {
    return {
      step: 1,
      email_val: '',
      code_val: '',
      showSpin: false
    }
  },
  methods: {
    cont () {
      this.showSpin = true
      setTimeout(() => {
        this.step = -1
        setTimeout(() => {
          this.showSpin = false
          this.step = 2
        }, 500)
      }, 1250)
    },
    cont2 () {
      if (!this.code_val.match(/[0-9]{6}/)) {
        alert('Error: Invalid code entered.')
        return
      }
      this.showSpin = true
      setTimeout(() => {
        this.step = -1
        setTimeout(() => {
          this.$router.push('/onboarding')
        }, 500)
      }, 1250)
    }
  }
}
</script>
