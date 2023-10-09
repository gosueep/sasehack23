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
// Provided by ChatGPT. Thanks!
const hobbiesAndInterests = [
  'Reading',
  'Hiking',
  'Cooking',
  'Painting',
  'Gardening',
  'Photography',
  'Swimming',
  'Playing a musical instrument',
  'Cycling',
  'Yoga',
  'Traveling',
  'Fishing',
  'Singing',
  'Dancing',
  'Drawing',
  'Watching movies',
  'Playing video games',
  'Birdwatching',
  'Knitting',
  'Writing',
  'Collecting stamps',
  'Playing chess',
  'Running',
  'Baking',
  'Sculpting',
  'Meditation',
  'Woodworking',
  'Skiing',
  'Camping',
  'Rock climbing'
]
const funEventsAndActivities = [
  'Concerts',
  'Sports games',
  'Festivals',
  'Movie nights',
  'Yoga days',
  'Picnics',
  'Amusement park visits',
  'Art gallery visits',
  'Karaoke night',
  'Board game night',
  'Trivia night',
  'Wine tasting',
  'Cooking classes',
  'Escape rooms',
  'Stand-up comedy shows',
  'Hiking trips',
  'Dance parties',
  'Cosplay conventions',
  'Scavenger hunts',
  'Cookouts'
]

export default {
  data: function () {
    return {
      isSubmitting: false,
      // Demographics
      i_name: '',
      i_loc: '',
      i_pronouns: '',
      // Hobbies and interests
      hobbiesAndInterests,
      selHobbies: [],
      // Events and activites
      funEventsAndActivities,
      selEvents: []
    }
  },
  methods: {
    async submit () {
      this.isSubmitting = true
      const resp = await fetch(`${this.$api_base_url}/create_user`, {
        method: 'post',
        body: JSON.stringify({
          name: this.i_name,
          location: this.i_loc,
          pronouns: this.i_pronouns,
          hobbies: this.selHobbies,
          events: this.selEvents
        })
      })
      const uid = await resp.json()
      console.log(uid)
      console.log(uid.user_id)
      localStorage.setItem('uid', uid.user_id)
      this.isSubmitting = false
      this.$router.push('/matching')
    }
  }
}
</script>
