<template>
    <div class="container" style="margin-bottom:30px">
        <form @submit.prevent ="createMessage">
            
            <div class="form-group">
                <input type="text" name="message" class="form-control" placeholder="Enter a message....." v-model="newMessage"> 
                <p class="text-danger" v-if="errorText">{{ errorText }}</p>
            </div>
            <button class="btn btn-danger " type ="submit" name="action">Send</button>
        </form>
    </div>
</template>
<script>
import firebaseApp from '@/firebase/init'

export default {
    name : 'CreateMessage',
    data(){
        return {
            newMessage : null,
            errorText : null 
        }
    },
    methods :{
        createMessage (){
            if(this.newMessage){
                firebaseApp.collection('messages').add({
                    messages : this.newMessage,
                    name :  window.username,
                    timestamp : Date.now(),
                

                }).catch(err =>  {
                    console.log(err);
                });
                this.newMessage = null;
                this.errorText = null ;
            }
            else { 
                this.errorText = "A message must be entered first";
            }
        }
    }
}
</script>
