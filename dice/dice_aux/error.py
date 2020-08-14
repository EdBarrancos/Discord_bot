class Error():
    async def defineError(self, errorMessage):
        self.errorMessage = errorMessage
        return self
        
    async def sendErrorToUser(self, context, helpCommand):
        await context.send(f"{context.author.mention}\n"
                           "{self.errorMessage}\n"
                           "For more information type {helpCommand}")
        return self

