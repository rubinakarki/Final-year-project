<template>
  <div class="container chat">
    <h2 class="text-center">Chatroom</h2>
    <div class="card">
      <div class="card-body" >
        <p class="text-secondary nomessages" v-if ="messages.length == 0">
          [No Messages yet!]
        </p>    
      <div class="messages" v-chat-scroll="{always: false,smooth :true}"> 
        <div v-for = "message in messages" :key ="message.id">
          <span class="text-danger">{{message.name}} : </span>
          <span>{{message.message}}</span>
          <span class="text-secondary time">{{message.timestamp}}</span>
          
        </div>

       </div>
      </div>
      <div class="card-action">
        <CreateMessage >
      </div>
    </div>
  </div>
</template>
<script>
// @ is an alias to /src
import  firebaseApp from '@/firebase/init';
import CreateMessage from '@/components/CreateMessage'
import moment from 'moment';

export default {    
 name: "Chat",
 data : () => ( 
   {
     messages : [],
   }
 ),
 components : {
   CreateMessage,
   },
  created(){
    let ref =firebaseApp.collection('messages').orderBy('timestamp');
    ref.onSnapshot(snapshot => {
      snapshot.docChanges().forEach(change =>{
        if(change.type = 'added'){
          let doc = change.doc;
          this.messages.push(
            { 
              id:doc.id,
              name: doc.data().name,
              message : doc.data().messages,
              timestamp :moment(doc.data().timestamp).format('LTS')
            }
          );
        }
      });
    });
  }

}
</script>
<style>
.card-body{
  background-color: #fffdd0;
}
.chat h2{
  font-size: 2.6em;
  margin-bottom: 0px;

}
.chat h5{
  margin-top: 0px;
  margin-bottom: 40px;
}

.chat .time{
  display : block ;
  font-size :0.7em;

}
.messages {
  max-height: 300px;
  overflow: auto;
}
</style>

