<template>
  <v-container>
    <h1>Add Tweet</h1>
    <br>
    <v-row>
      <v-col cols="7">
        <v-text-field variant="outlined" v-model="tweet" label="Tweet" placeholder="Your tweet..."></v-text-field>
      </v-col>
      <v-col sm="3">
        <v-text-field variant="outlined" v-model="name" label="Name" placeholder="Your name..."></v-text-field>
      </v-col>
      <v-col md="2">
        <v-btn color="blue" size="x-large" @click="submitTweet">Post</v-btn>
      </v-col>
    </v-row>
  </v-container>

  <v-container>
    <h1>Tweets</h1>
    <v-table>
      <thead>
        <tr>
          <th class="text-left">
            <h3 class="sort" @click="sortData('name')">
              Name
              <v-icon>mdi-sort</v-icon>
            </h3>
          </th>
          <th class="text-left">
            <h3>Tweet</h3>
          </th>
          <th class="text-center">
            <h3 class="sort" @click="sortData('created_at')">
              Created at
              <v-icon>mdi-sort</v-icon>
            </h3>
          </th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in tweets" :key="item.id">
          <td>{{ item.name }}</td>
          <td>{{ item.message }}</td>
          <td class="text-center">{{ getDate(item.created_at) }}</td>
        </tr>
      </tbody>
    </v-table>
  </v-container>

</template>

<script src="./index.js"></script>
<style scoped src="./style.css"></style>
