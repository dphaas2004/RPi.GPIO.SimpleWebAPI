RPi = {
    GPIO:{
        Init: async ()=>{
            let response = await fetch('/cgi-bin/GPIO.py?'+ new URLSearchParams({
                Action: 'Init',
            }))
            let Value = await response.text();
            return Value
        },
        Mode:{
            Get: async ()=>{
                let response = await fetch('/cgi-bin/GPIO.py?'+ new URLSearchParams({
                    Action: 'Mode'
                }))
                let Value = await response.text();
                return Value
            },
            Set: async (Val)=>{
                let response = await fetch('/cgi-bin/GPIO.py?'+ new URLSearchParams({
                    Action: 'Mode',
                    Value: Val
                }))
                let Value = await response.text();
                return Value
            }
        },
        Get: async (Pin)=>{
            if(!Pin) new Error('Error Initializing Pin Get');
            let response = await fetch('/cgi-bin/GPIO.py?'+ new URLSearchParams({
                Pin: Pin,
                Action: 'Get'
            }))
            let Value = await response.text();
            return Value
        },
        Set: async (Pin,State)=>{
            if(!(Pin&&State)) new Error('Error Initializing Pin Set');
            let response = await fetch('/cgi-bin/GPIO.py?'+ new URLSearchParams({
                Pin: Pin,
                Action: 'Set',
                Value: State
            }))
            let Value = await response.text();
            return Value
        },
        Setup:(Pin, Type)=>{
            if(!(Pin && Type)) new Error('Error Initializing Pin Set');
        }
    }
}