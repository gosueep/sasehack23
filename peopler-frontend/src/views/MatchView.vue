<template>
  <TransitionGroup>
    <p class='loading' v-if='loading===1'><fa-icon icon='fas fa-fw fa-circle-notch' spin></fa-icon> We're finding matches for you. This may take a minute...</p>
    <p class='loading' v-if='loading===2'><fa-icon icon='fas fa-fw fa-check'></fa-icon> Matches found!</p>
  </TransitionGroup>
  <Transition>
    <div id='matches' v-if='loading===0'>
      <h1>We found matches!</h1>
      <p>Select a person that you'd like to connect with.<br/>Don't worry, you'll be able to connect with more people afterwards.</p>
      <div id='pf-outer'>
        <ProfileBox v-for='(pf, i) in profiles' v-bind:key='pf.name'>
          <template #header><h1 style='margin-bottom: 10px'>{{ pf.name }}</h1><p class='pf-pn'><i>{{ pf.pronouns }}</i></p></template>
          <p class='pf-p'>{{ pf.desc }}</p>
          <button @click='connect(i)'>Connect with {{ pf.name }}</button>
        </ProfileBox>
      </div>
    </div>
  </Transition>
</template>

<style scoped>
.btnlist-outer button {
  margin-right: 8px;
  margin-bottom: 8px;
}

.loading {
  font-size: 20px;
  text-align: center;
  margin: 72px 0;
}

#matches {
  text-align: center;
}

#matches h1 {
  font-weight: 600;
}

#pf-outer {
  display: flex;
  justify-content: space-between;
}

#pf-outer div {
  flex-grow: 1;
  margin: 12px;
}

.pf-pn {
  color: #777;
  margin-top: 0
}

.pf-p {
  min-height: 300px;
}
</style>

<script>
import ProfileBox from '@/components/ProfileBox.vue'

async function _delay (ms) {
  // eslint-disable-next-line
  return new Promise(r => setTimeout(r, ms))
}

export default {
  components: {
    ProfileBox
  },
  data: function () {
    return {
      loading: 1,
      profiles: []
    }
  },
  created: async function () {
    await this.getMatch()
  },
  methods: {
    async getMatch () {
      this.loading = 1
      // const resp = await fetch(`${this.$api_base_url}/get_match`, {
      //   method: 'post',
      //   body: JSON.stringify({
      //     user_id: this.i_name
      //   })
      // })
      // console.log(resp)

      // eslint-disable-next-line camelcase
      async function _DEV_TMP_FakeResponse () {
      // eslint-disable-next-line promise/param-names
        await _delay(2400)
        return {
          profiles: [
            {
              name: 'Bob',
              pronouns: 'they/them',
              desc: 'Meet Bob, an adventurous spirit like you. They share your love for hiking and skiing, making them a great match for outdoor activities. Explore new heights together!'
            },
            {
              name: 'Will',
              pronouns: 'he/him',
              desc: "Meet Will, an adventurous and intellectually stimulating individual who shares your love for chess. With a passion for camping, skiing, and rock climbing, Will's zest for life will surely captivate you. Join him for exciting cosplay conventions and trivia nights!"
            },
            {
              name: 'Eugin',
              pronouns: 'he/him',
              desc: "Meet Eugin, an artistic soul like you. They share your passion for sculpting and art gallery visits. Eugin's love for drawing and gardening adds a creative twist to their life. Connect over shared interests!"
            }
          ]
        }
      }
      const resp = await _DEV_TMP_FakeResponse()
      this.profiles = resp.profiles

      this.loading = 3
      await _delay(480)
      this.loading = 2
      await _delay(1500)
      this.loading = 3
      await _delay(480)
      this.loading = 0
    },
    connect (i) {
      alert(`The connect button was pressed for: ${this.profiles[i].name}\n\nFeature to be implemented.`)
    }
  }
}
</script>
