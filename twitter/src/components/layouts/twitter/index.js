import axios from "axios"
export default {
  name: 'twitter-component',

  data: () => ({
    tweet: "",
    name: "",
    ascending: "",
    tweets: [
    ],
  }),

  mounted() {
    this.getTweets()
  },

  methods: {
    submitTweet() {
      axios.post(process.env.VUE_APP_BACKEND_URL + '/twitter/api', { name: this.name, message: this.tweet })
        .then(response => {
          this.getTweets();     // getting lastest tweets after successfull tweet submission
        })
        .catch(err => (
          console.error(err.response.data.detail)
        ))
    },

    // getting tweets data
    getTweets() {
      axios.get(process.env.VUE_APP_BACKEND_URL + '/twitter/api')
        .then(response => (this.tweets = response.data))
        .catch(err => (
          console.error(err.response.data.detail)
        ))
    },

    // converting time into locale date string
    getDate(date) {
      let d = new Date(date)
      return d.toLocaleDateString()
    },
  
  // For Sorting Data
  sortData(column){
    if(this.ascending == false || this.ascending == ""){
      this.ascending = true
      this.tweets.sort((a, b) => a[column].localeCompare(b[column]));
    }
    else{
      this.ascending = false
      this.tweets.sort((a, b) => b[column].localeCompare(a[column]));
    }
  },
},
}