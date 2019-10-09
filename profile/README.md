# Profile APIs

##### normal
firmware.get('dtb')    
firmware.set('dtb', value=value)    
firmware.get('kernel')  
firmware.set('kernel', value=value)  

firmware.get('image_type')  
firmware.set('image_type', value=image_type)  
firmware.get('image_path')  
firmware.set('image_path', value=image_path)  

firmware.get('toh')    
firmware.set('toh', value=value)    

firmware.get('profile')
firmware.set('profile')
firmware.get('architecture')  
firmware.set('architecture', value=value, confidence=1)  

firmware.get('brand')  
firmware.set('brand', value=value)  
firmware.get('revision')  
firmware.set('revision', value=value)  
firmware.get('target')  
firmware.set('target', value=value)  
firmware.get('subtarget')  
firmware.set('subtarget', value=value)  

firmware.get('kernel_load_address')  
firmware.set('kernel_load_address', value=value)  
firmware.get('kernel_version')  
firmware.set('kernel_version', value=value )  
firmware.get('kernel_created_time')  
firmware.set('kernel_created_time', value=value, confidence=1)  
firmware.get('kernel_entry_point')  
firmware.set('kernel_entry_point', value=value, confidence=1)  
##### CPU
firmware.get('cpu', key='model')  
firmware.set('cpu', key='model', value=value, confidence=1)  
firmware.set('cpu', key='qemu', value=value, confidence=1)  
firmware.set('cpu_priv', key='qemu', value=value, confidence=1)  
##### RAM
firmware.set('ram', key='size')  
firmware.set('ram', key='start', value=value, confidence=1)  
firmware.set('ram', key='size', value=value, confidence=1)  
##### IC
firmware.set('ic', key='model')  
firmware.set('ic', key='model', value=value, confidence=1)  
firmware.set('ic', key='qemu', value=value, confidence=1)  
##### FLASH
firmware.get('flash', key='type')  
firmware.set('flash', key='type', value=value, confidence=1)  
firmware.set('flash', key='model', value=value, confidence=1)  
firmware.set('flash', key='qemu', value=value, confidence=1)  
##### UART
firmware.get('uart', key='model')  
firmware.set('uart', key='model', value=value, confidence=1)  
firmware.set('uart', key='qemu', value=value, confidence=1) 
