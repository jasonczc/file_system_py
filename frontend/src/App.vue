<template>
  <v-app>
    <v-main>
        <v-card>
          <v-card-title>
            File Manager {{nowPath}}
          </v-card-title>
          <v-row align="center">
            <v-btn @click="refresh" class="transparent elevation-0">
              <v-icon>
                mdi-refresh
              </v-icon>
              REFRESH
            </v-btn>
            <v-btn @click="nowPath = '/';refresh()" class="transparent elevation-0">
              <v-icon>
                mdi-home
              </v-icon>
              HOME
            </v-btn>
            <v-btn v-if="nowPath!=='/'" @click="backFolder();refresh()" class="transparent elevation-0">
              <v-icon>
                mdi-arrow-left
              </v-icon>
              BACK
            </v-btn>
            <v-col cols="3" align-self="center">
            <v-text-field label="folder name" v-model="pathname"></v-text-field>
            </v-col>
            <v-btn @click="mkdir" class="transparent elevation-0">
              <v-icon>
                mdi-plus
              </v-icon>
              CREATE FOLDER
            </v-btn>
          </v-row>
          <v-simple-table>
        <template v-slot:default>
          <thead>
               <tr>
                <th class="text-left">
                  Name
                </th>
                <th class="text-left">
                 type
                </th>
                 <th class="text-left">
                 create_time
                </th>
                 <th class="text-left">
                 action
                </th>
        </tr>
      </thead>
      <tbody>
        <tr
          v-for="item in fileList"
          :key="item.name"
        >
          <td>{{ item.name }}</td>
          <td>{{ item.tag==='0'?'file':'folder' }}</td>
          <td>{{ new Date(item.create_time*1000).toISOString() }}</td>
          <td>
            <v-btn icon @click="del(item.name)">
              <v-icon>
                mdi-delete
              </v-icon>
            </v-btn>
            <v-btn icon v-if="item.tag===1" @click="appendFolder(item.name);refresh()">
              <v-icon>
                mdi-arrow-right
              </v-icon>
            </v-btn>
          </td>
        </tr>
      </tbody>
    </template>
  </v-simple-table>
        </v-card>
    </v-main>
  </v-app>
</template>

<script>

import request from "@/lib/request";
export default {
  name: 'App',
  data: () => {
    return {
      nowPath: "/",
      fileList: [],
      pathname: "",
    }
  },
  mounted() {
    this.refresh()
  },
  methods: {
    backFolder() {
      let index = 0
      for (let i = this.nowPath.length - 1; i >= 0; i--) {
        if (this.nowPath[i] === '/') {
          index = i;
          break
        }
      }
      if (index === 0) this.nowPath = '/';
      else {
        this.nowPath = this.nowPath.substr(0, index)
      }
    },
    appendFolder(name) {
      if (this.nowPath[this.nowPath.length - 1] === '/')
        this.nowPath += name
      else this.nowPath += '/' + name
    },
    refresh() {
      request({
        url: 'ls?path=' + this.nowPath,
        method: "get"
      }).then((res) => {
        this.fileList = res.data
      })
    },
    del(filename) {
      request({
        url: 'del?path=' + this.nowPath + '/' + filename,
        method: "get"
      }).then((res) => {
        this.refresh()
      })
    },
    mkdir() {
      request({
        url: 'mkdir?path=' + (this.nowPath==='/'?'':this.nowPath) + '/' + this.pathname,
        method: "get"
      }).then((res) => {
        this.refresh()
      })
    }
  }
};
</script>
