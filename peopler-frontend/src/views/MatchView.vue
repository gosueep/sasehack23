<template>
  <h1>Peopler</h1>
  <p>Welcome to Peopler. Let's get you set up with your profile, and soon you'll be on your way to matching with new people!</p>

  <h2>1. Basic Information</h2>
  <p><input v-model='i_name' placeholder='Full Name'/> What's your name?</p>
  <p><input v-model='i_pronouns' placeholder='Pronouns'/> What pronouns do you go by? (i.e., she/her, them/them, he/him, etc.)</p>
  <p><input v-model='i_loc' placeholder='City, State'/> What area do you live in?</p>

  <h2>2. Hobbies and Interests</h2>
  <p>We'll try to match you with someone who shares things in common with you. Please select everything that you enjoy or regularly partake in.</p>
  <div class='btnlist-outer'>
    <span v-for='i in hobbiesAndInterests' v-bind:key='i'>
      <button @click='selHobbies.splice(selHobbies.indexOf(i), 1)' v-if='selHobbies.includes(i)'><fa-icon icon='fas fa-square-check'></fa-icon> {{ i }}</button>
      <button @click='selHobbies.push(i)' class='btn-gray' v-else><fa-icon icon='far fa-square'></fa-icon> {{ i }}</button>
    </span>
  </div>

  <h2>3. Existing Events</h2>
  <p>If there's activities you already partake in, we'll try to steer our recommendations towards those activities or similar ones.</p>
  <div class='btnlist-outer'>
    <span v-for='i in funEventsAndActivities' v-bind:key='i'>
      <button @click='selEvents.splice(selEvents.indexOf(i), 1)' v-if='selEvents.includes(i)'><fa-icon icon='fas fa-square-check'></fa-icon> {{ i }}</button>
      <button @click='selEvents.push(i)' class='btn-gray' v-else><fa-icon icon='far fa-square'></fa-icon> {{ i }}</button>
    </span>
  </div>

  <p>Once you've finished, hit "Submit" and we'll match you up!</p>
  <p><button @click='submit' :disabled='isSubmitting'>Submit</button> <Transition><span v-if='isSubmitting'> &nbsp;<fa-icon icon='fas fa-fw fa-circle-notch' spin></fa-icon> Please wait as your information is being submitted.</span></Transition></p>

</template>

<style scoped>
.btnlist-outer button {
  margin-right: 8px;
  margin-bottom: 8px;
}
</style>

<script>

export default {
  data: function () {
    return {
      isSubmitting: false,
      // Demographics
      i_name: '',
      i_loc: '',
      i_pronouns: '',
      // Hobbies and interests
      selHobbies: [],
      // Events and activites
      selEvents: []
    }
  },
  methods: {
    async getMatch () {
      this.loading = true
      const resp = await fetch(`${this.$api_base_url}/get_match`, {
        method: 'post',
        body: JSON.stringify({
          user_id: this.i_name
        })
      })
      console.log(resp)
      this.loading = false
      this.$router.push('/matching')
    }
  }
}
</script>
