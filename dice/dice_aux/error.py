class Error():
    async def defineError(self, errorMessage: str):
        self.errorMessage = errorMessage
        return self
        
    async def sendErrorToUser(self, context, helpCommand: str):
        await context.send(f'{context.author.mention}\n{self.errorMessage}\nFor more information type {helpCommand}')
        return self

