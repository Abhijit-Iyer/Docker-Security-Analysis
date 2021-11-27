f = open("/usr/app/src/File from host.txt", 'r+', encoding = 'utf-8') 

print("\n\t The host file has successfully been opened! Here's a security breach!")

file_content = f.read()

print("\n\t Printing what is written in the host's file.")

print("\n\t ", file_content)

f.close()

f = open("/usr/app/src/File from container.txt", 'w', encoding = 'utf-8') 

f.write("\n\t Hello, I'm the container! Pleased to meet you, host! ")

print("\n\t A file has been created by the container and some content has been written onto it by the container. The changes are visible in the host too. Check it out! Breach of security!")

f.close()

# print("Hello World")