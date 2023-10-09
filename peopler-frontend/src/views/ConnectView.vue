<template>
  <div id='cv-out'>
    <ProfileBox id='pfb'>
      <template #header>
        <div class='hd'>
          <p style='font-size: 24px'><b>{{ profile.name }}</b> <i>{{ profile.pronouns }}</i></p>
          <p style='color: #195d1b'><fa-icon icon='far fa-circle-check'></fa-icon> Currently Online</p>
        </div>
      </template>
      <div id='flex-l'>
        <div style='flex-grow: 1;'><p>Meet Will, an adventurous and intellectually stimulating individual who shares your love for chess. With a passion for camping, skiing, and rock climbing, Will's zest for life will surely captivate you. Join him for exciting cosplay conventions and trivia nights!</p><p>Will is interested in playing chess, camping, skiing, and rock climbing.</p></div>
        <div><a href='#'><fa-icon icon='fas fa-arrow-left'></fa-icon> Exit this chat </a></div>
      </div>
    </ProfileBox>
    <div id='chat'>
      <div id='chat-msgs'>
        <TransitionGroup>
          <div v-if='showOnboarding' id='p-onboarding'><b>Welcome to chat!</b><br/>Use this space to connect with new people and find community!<br/>
            <p>Need some inspiration to craft your first message?<br/><a @click='showRecs = !showRecs'>{{ showRecs ? 'Hide' : 'Show' }} Recommendations</a> | <a @click='showOnboarding = false'>Dismiss Welcome Message</a></p>
            <p></p>
            <p style='text-align: left' v-if='showRecs'>
              <span>Here's some recommendations on what you can reach out about, based on your shared interests and background:</span><br/>
              <ul>
                <li>Since you both enjoy playing chess, why not organize a chess tournament? You can find a local chess club or even set up a game at a park. It will be a fun and intellectually stimulating activity for both of you.</li>
                <li>Since you enjoy reading and Will enjoys camping, how about organizing a book club camping trip? You can choose a book that interests both of you and spend a weekend in nature discussing the book around a campfire. It will be a unique and adventurous experience.</li>
                <li>              If you're both into hiking, why not plan a hiking trip to a nearby national park or nature reserve? You can explore new trails, enjoy the beautiful scenery, and have some quality time together while getting some exercise.
                </li>
              </ul>
            </p>
          </div>
          <p v-for='msg in messages' v-bind:key='msg.msg'><b>{{ msg.from }}</b> {{ msg.msg }}</p>
        </TransitionGroup>
      </div>
      <input v-model='i_msg' @keyup.enter='sendMsg' placeholder='Type a message, use enter to send...'/>
    </div>
  </div>
</template>
<style scoped>
a {
  text-decoration: none;
  color: #009ac4;
  cursor: pointer;
}

#pfb {
  width: 300px;
  flex-shrink: 0;
}

#flex-l {
  height: calc(100% - 115px);
  display: flex;
  flex-direction: column;
}

#p-onboarding {
  padding: 8px 16px;
  text-align: center;
  background-color: #ffffff3f;
  border-radius: 8px;
}

#cv-out {
  display: flex;
}

#chat {
  flex-grow: 1;
  margin-left: 16px;
  display: flex;
  flex-direction: column;
}

#chat-msgs {
  flex-grow: 1;
  overflow-y: scroll;
}

#chat input {
  width: 100%;
  box-sizing: border-box;
}

#cv-out > div {
  height: 90vh;
  overflow-y: auto;
}

.hd p {
  line-height: 0.5;
}
</style>

<script>
import ProfileBox from '@/components/ProfileBox.vue'

export default {
  components: {
    ProfileBox
  },
  data: function () {
    return {
      profile: {},
      messages: [],
      i_msg: '',
      showOnboarding: true,
      showRecs: false
    }
  },
  created () {
    // TODO: Pull this from the API
    this.profile = {
      name: 'Will',
      pronouns: 'he/him',
      desc: "Meet Will, an adventurous and intellectually stimulating individual who shares your love for chess. With a passion for camping, skiing, and rock climbing, Will's zest for life will surely captivate you. Join him for exciting cosplay conventions and trivia nights!"
    }
  },
  methods: {
    sendMsg () {
      this.messages.push({ from: 'You', msg: this.i_msg })
      this.i_msg = ''
      document.getElementById('chat-msgs').scrollTo(0, 1e9)
      setTimeout(() => { document.getElementById('chat-msgs').scrollTo(0, 1e9) }, 50)
    }
  }
}
</script>
