import discord
from discord.ext import commands


col = discord.Color.purple()

class HelpCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

# * -------------------------------------------------------------------   
        
    @commands.Cog.listener()
    async def on_ready(self):
        print("Help command is online")

# * -------------------------------------------------------------------           
        
        
    @commands.hybrid_command(name='help', description='Shows a list of commands')
    async def help(self, ctx, cmd=None):
        
# * -------------------------------------------------------------------           
        
        #^DSA
        
        if cmd is None:
            embed = discord.Embed(
                description="""Here is the list of commands!
        For more info on a specific command, use `!help {command}`""",
                color=col
            )
            embed.set_author(name="Command List", icon_url=ctx.author.display_avatar.url)
            # Loop through the cogs (top-level commands)
            for cog in self.bot.cogs:
                embed.add_field(name=cog, value=', '.join(f"`{cmd.name}`" for cmd in self.bot.get_cog(cog).get_commands() if not cmd.parent), inline=False)             # only those commands that don't have a parent will be displayed; since subcommands have parent, they won't show

            await ctx.send(embed=embed)
            
            
        elif cmd == "searching":
            embed = discord.Embed(
                description="Contains searching command, code for linear and binary search",
                color=col
            )
            embed.set_author(name="Searching element", icon_url=ctx.author.display_avatar.url)
            embed.add_field(name = "Search an element in a array",value = """Provide element and an array to work
                            Syntax: `!searching search_element element array`
                            Example: `!searching search_element {1} {1 2 3 4 5}`""", inline=False)
            
            embed.add_field(name = "Linear search code",value = """Provides code for linear search in python or cpp
                            Syntax: `!searching linear_search_code {python/cpp}`""", inline=False)
            
            embed.add_field(name = "Binary search code",value = """Provides code for binary search in python or cpp
                            Syntax: `!searching binary_search_code {python/cpp}`""", inline=False)
            await ctx.send(embed = embed)
            
            
        elif cmd == "sorting":
            embed = discord.Embed(
                description="Contains sorting command and code for all sorting algorithms",
                color=col
            )
            embed.set_author(name="Sorting an array", icon_url=ctx.author.display_avatar.url)
            embed.add_field(name = "sort",value = """Sorts an array of n elements
                            Syntax: `!sorting sort {array}`
                            Example: `!sorting sort {9 8 7 6 5 4 3 2 1}`""", inline=False)
            
            embed.add_field(name = "bubble_sort_code",value = """Provides code for bubble sort in python or cpp
                            Syntax: `!sorting bubble_sort_code {python/cpp}`""", inline=False)
            
            embed.add_field(name = "selection_sort_code",value = """Provides code for selection sort in python or cpp
                            Syntax: `!sorting selection_sort_code {python/cpp}`""", inline=False)
            
            embed.add_field(name = "insertion_sort_code",value = """Provides code for insertion sort in python or cpp
                            Syntax: `!sorting insertion_sort_code {python/cpp}`""", inline=False)
            
            embed.add_field(name = "quick_sort_code",value = """Provides code for quick sort in python or cpp
                            Syntax: `!sorting quick_sort_code {python/cpp}`""", inline=False)
            
            embed.add_field(name = "merge_sort_code",value = """Provides code for merge sort in python or cpp
                            Syntax: `!sorting merge_sort_code {python/cpp}`""", inline=False)
            
            await ctx.send(embed = embed)
            
            
        elif cmd == "linked_list":
            embed = discord.Embed(
                description="Contains codes for linked list operations",
                color=col
            )
            embed.set_author(name="Linked List operations", icon_url=ctx.author.display_avatar.url)
            embed.add_field(name = "head_insertion_code",value = """Inserts a node at head
                            Syntax: `!linked_list head_insertion_code {python/cpp}`
                            """, inline=False)
            
            embed.add_field(name = "tail_insertion_code",value = """Inserts a node at tail
                            Syntax: `!linked_list tail_insertion_code {python/cpp}`
                            """, inline=False)
            
            embed.add_field(name = "position_insertion_code",value = """Inserts a node at any position
                            Syntax: `!linked_list position_insertion_code {python/cpp}`
                            """, inline=False)
            
            embed.add_field(name = "deletion_at_beginning",value = """Deletes a node at beginning
                            Syntax: `!linked_list deletion_at_beginning {python/cpp}`
                            """, inline=False)
            
            embed.add_field(name = "deletion_at_end",value = """Deletes a node at end
                            Syntax: `!linked_list deletion_at_end {python/cpp}`
                            """, inline=False)
            
            embed.add_field(name = "deletion_at_position",value = """Deletes a node at specified position
                            Syntax: `!linked_list deletion_at_position {python/cpp}`
                            """, inline=False)
            
            embed.add_field(name = "reversal_code",value = """Reverses a linked list
                            Syntax: `!linked_list reversal_code {python/cpp}`
                            """, inline=False)
            
            await ctx.send(embed = embed)
            
            
        elif cmd == "stack":
            embed = discord.Embed(
                description="Contains codes for stack operations",
                color=col
            )
            embed.set_author(name="Stack operations operations", icon_url=ctx.author.display_avatar.url)
            embed.add_field(name = "implement",value = """Provides code for stack implementation
                            Syntax: `!stack implement {python/cpp}`
                            """, inline=False)
            
            embed.add_field(name = "reverse",value = """Provides code for reversing a stack
                            Syntax: `!stack reverse {python/cpp}`
                            """, inline=False)
            
            await ctx.send(embed = embed)
            
            
        elif cmd == "queue":
            embed = discord.Embed(
                description="Contains codes for queue operations",
                color=col
            )
            embed.set_author(name="Queue operations operations", icon_url=ctx.author.display_avatar.url)
            embed.add_field(name = "implement",value = """Provides code for queue implementation
                            Syntax: `!queue implement {python/cpp}`
                            """, inline=False)
            
            embed.add_field(name = "reverse",value = """Provides code for reversing a queue
                            Syntax: `!queue reverse {python/cpp}`
                            """, inline=False)
            
            await ctx.send(embed = embed)
            
# * -------------------------------------------------------------------   
        
        #^DSA visualizer
        
        elif cmd == "visual_search":
            embed = discord.Embed(
                description="Provides a static visualizer for searching algorithms",
                color=col
            )
            embed.set_author(name="Searching visualizer for both linear and binary search", icon_url=ctx.author.display_avatar.url)
            embed.add_field(name = "linear_search",value = """Provides a static visualizer for linear search
                            Syntax: `!visual_search linear_search`
                            """, inline=False)
            
            embed.add_field(name = "binary_search",value = """Provides a static visualizer for binary search
                            Syntax: `!visual_search binary_search`
                            """, inline=False)
            
            await ctx.send(embed = embed)
        
        
        elif cmd == "visual_sort":
            embed = discord.Embed(
                description="Provides a static visualizer for sorting algorithms",
                color=col
            )
            embed.set_author(name="Sorting visualizer for all sorting algorithms", icon_url=ctx.author.display_avatar.url)
            embed.add_field(name = "bubble_sort",value = """Provides a static visualizer for bubble sort
                            Syntax: `!visual_sort bubble_sort`
                            """, inline=False)
            
            embed.add_field(name = "selection_sort",value = """Provides a static visualizer for selection sort
                            Syntax: `!visual_sort selection_sort`
                            """, inline=False)
            
            embed.add_field(name = "insertion_sort",value = """Provides a static visualizer for insertion sort
                            Syntax: `visual_sort insertion_sort`
                            """, inline=False)
            
            embed.add_field(name = "quick_sort",value = """Provides a static visualizer for quick sort
                            Syntax: `visual_sort quick_sort`
                            """, inline=False)
            
            embed.add_field(name = "merge_sort",value = """Provides a static visualizer for merge sort
                            Syntax: `visual_sort merge_sort`
                            """, inline=False)
            
            await ctx.send(embed = embed)
        
        
        elif cmd == "LL_visual":
            embed = discord.Embed(
                description="Provides a static visualizer for Linked List operations",
                color=col
            )
            embed.set_author(name="Linked List visualizer for operations on it", icon_url=ctx.author.display_avatar.url)
            embed.add_field(name = "singly_insertion",value = """Provides a static visualizer for insertion on singly linked list
                            Syntax: `!LL_visual singly_insertion`
                            """, inline=False)
            
            embed.add_field(name = "singly_deletion",value = """Provides a static visualizer for deletion on singly linked list
                            Syntax: `!LL_visual singly_deletion`
                            """, inline=False)
            
            embed.add_field(name = "doubly_insertion",value = """Provides a static visualizer for insertion on doubly linked list
                            Syntax: `!LL_visual doubly_insertion`
                            """, inline=False)
            
            embed.add_field(name = "doubly_deletion",value = """Provides a static visualizer for deletion on doubly linked list
                            Syntax: `!LL_visual doubly_deletion`
                            """, inline=False)
            
            embed.add_field(name = "circular_insertion",value = """Provides a static visualizer for insertion on circular linked list
                            Syntax: `!LL_visual circular_insertion`
                            """, inline=False)
            
            embed.add_field(name = "circular_deletion",value = """Provides a static visualizer for deletion on circular linked list
                            Syntax: `!LL_visual circular_deletion`
                            """, inline=False)
            
            await ctx.send(embed = embed)
        
        
        elif cmd == "visual_stack":
            embed = discord.Embed(
                description="Provides a static visualizer for operations on stack",
                color=col
            )
            embed.set_author(name="Stack visualizer for its operations", icon_url=ctx.author.display_avatar.url)
            embed.add_field(name = "stack_visual",value = """Provides a static visualizer for operations on stack
                            Syntax: `!visual_stack stack_visual`
                            """, inline=False)
            
            await ctx.send(embed = embed)
            
            
        elif cmd == "visual_queue":
            embed = discord.Embed(
                description="Provides a static visualizer for operations on queue",
                color=col
            )
            embed.set_author(name="Queue visualizer for its operations", icon_url=ctx.author.display_avatar.url)
            embed.add_field(name = "queue_visual",value = """Provides a static visualizer for operations on queue
                            Syntax: `!visual_queue queue_visual`
                            """, inline=False)
            
            await ctx.send(embed = embed)
            
# * -------------------------------------------------------------------   


    #^ ECONOMY
    
        elif cmd == "cflip" or cmd == "cf":
            embed = discord.Embed(
                description="""A simple coinflip command to get easy credits
                If flip result is same as picked choice, the user will get the coins he bet else he'll lose the coins
                
                Alaises = cf
                """,
                color=col 
            )
            embed.set_author(name="Coin flip", icon_url=ctx.author.display_avatar.url)
            embed.add_field(name = "cflip",value = """
                            
                            Syntax: `!{cflip | cf} {heads | tails} {amount}`
                            
                            Example: `!cf h 100`""", inline=False)
            
            await ctx.send(embed = embed)
    
    
        elif cmd == "balance" or cmd == "bal":
            embed = discord.Embed(
                description="""A command to view both your cash and bank credits

                Alaises = bal
                """,
                color=col 
            )
            embed.set_author(name="Balance", icon_url=ctx.author.display_avatar.url)
            embed.add_field(name = "balance",value = """
                            
                            Syntax: `!{balance | bal}`
                            
                            Example: `!bal`""", inline=False)
            
            await ctx.send(embed = embed)
    
    
        elif cmd == "beg":
            embed = discord.Embed(
                description="""A simple command to get easy credits
                
                Has a failure probability and user may also get stolen from!
                
                Works with a cooldown of 10 minutes
                """,
                color=col 
            )
            embed.set_author(name="Beg", icon_url=ctx.author.display_avatar.url)
            embed.add_field(name = "beg",value = """
                            
                            Syntax: `!{beg} `""", inline=False)
            
            await ctx.send(embed = embed)
    
    
        elif cmd == "work":
            embed = discord.Embed(
                description="""A simple command to get easy credits
                
                Works with a cooldown of 1 hour   
                """,
                color=col 
            )
            embed.set_author(name="Work", icon_url=ctx.author.display_avatar.url)
            embed.add_field(name = "work",value = """
                            
                            Syntax: `!{work} `""", inline=False)
            
            await ctx.send(embed = embed)
    
    
        elif cmd == "deposit" or cmd == "dep":
            embed = discord.Embed(
                description="""Used to transfer credits from cash to bank  
                
                alaises = dep
                """,
                color=col 
            )
            embed.set_author(name="Deposit", icon_url=ctx.author.display_avatar.url)
            embed.add_field(name = "deposit",value = """
                            
                            Syntax: `!{deposit | dep} amount`""", inline=False)
            
            await ctx.send(embed = embed)
    
    
        elif cmd == "withdraw" or cmd == "wd":
            embed = discord.Embed(
                description="""Used to withdraw credits from bank to cash  
                
                alaises = wd
                """,
                color=col 
            )
            embed.set_author(name="Withdraw", icon_url=ctx.author.display_avatar.url)
            embed.add_field(name = "withdraw",value = """
                            
                            Syntax: `!{withdraw | wd} amount`""", inline=False)
            
            await ctx.send(embed = embed)
    
    
        elif cmd == "steal":
            embed = discord.Embed(
                description="""Used to interact with credits from another person
                
                Only works if user has credits in cash
                
                Has a failure probability and user can steal some amount or even get stolen from!
                """,
                color=col 
            )
            embed.set_author(name="Steal", icon_url=ctx.author.display_avatar.url)
            embed.add_field(name = "steal",value = """
                            
                            Syntax: `!{steal} @member_tag`""", inline=False)
            
            await ctx.send(embed = embed)
            
            
        elif cmd == "daily":
            embed = discord.Embed(
                description=""" Used to get a certain amount of coins on a daily basis
                
                Has a cooldown of 24 hours
                
                Maintaining a daily streak will increase the number of coins the user gets
                """,
                color=col 
            )
            embed.set_author(name="Daily", icon_url=ctx.author.display_avatar.url)
            embed.add_field(name = "daily",value = """
                            
                            Syntax: `!{daily}`""", inline=False)
            
            await ctx.send(embed = embed)
            
            
# * -------------------------------------------------------------------   
        
        
        #^ Fun commands
        
        elif cmd == "fun":
            embed = discord.Embed(
                description="""### Description
Express your emotions on others!""",
                color=col
            )
            embed.set_author(name="Fun/Casual Commands", icon_url=ctx.author.display_avatar.url)
            embed.add_field(name = "slap",value = """
                            Syntax: `!fun slap {@mention_user} {reason}`
                           """, inline=False)
            
            embed.add_field(name = "say",value = """Someone's gotta play Simon Says, right?
                            Syntax: `!fun say {content}`""", inline=False)
            
            embed.add_field(name = "choice",value = """Provide with a bunch of options to choose from
                            Syntax: `!fun choice {options}`""", inline=False)
            
            await ctx.send(embed = embed)
        
        
# * -------------------------------------------------------------------   


        #^ levelSystem command
        
        elif cmd == "level" or cmd == "rank" or cmd == "lvl":
            embed = discord.Embed(
                description="""Check your level in the server!
                
                alaises = [level | rank | lvl]""",
                color=col
            )
            embed.set_author(name="Level Commands", icon_url=ctx.author.display_avatar.url)
            
            embed.add_field(name = "level",value = """Provide with a bunch of options to choose from
                            Syntax: `!level {@mention_user}`""", inline=False)
            
            await ctx.send(embed = embed)
            

# * -------------------------------------------------------------------   


        #^math
        
        elif cmd == "math":
            embed = discord.Embed(
                description="""Contains mathematical operations
                """,
                color=col
            )
            embed.set_author(name="Math commands", icon_url=ctx.author.display_avatar.url)
            
            embed.add_field(name = "add",value = """Adds a given set of nunmbers
                            Syntax: `!add {numbers}`""", inline=False)
            
            embed.add_field(name = "subtract",value = """Subtracts a given set of nunmbers
                            Syntax: `!subtract {numbers}`""", inline=False)
            
            embed.add_field(name = "multiply",value = """Multiplies a given set of nunmbers
                            Syntax: `!multiply {numbers}`""", inline=False)
            
            embed.add_field(name = "divide",value = """Divides a given set of nunmbers
                            Syntax: `!divide {numbers}`""", inline=False)
            
            embed.add_field(name = "exponent",value = """Gives exponentiation of 2 nunmbers
                            Syntax: `!exponent {number_1} {number_2}`""", inline=False)
            
            embed.add_field(name = "mean",value = """Calculates the mean (average) of the given data
                            Syntax: `!mean {numbers}`""", inline=False)
            
            embed.add_field(name = "harmonic_mean",value = """Calculates the harmonic mean (central location) of the given data
                            Syntax: `!harmonic_mean {numbers}`""", inline=False)
            
            embed.add_field(name = "median",value = """Calculates the median (middle value) of the given data
                            Syntax: `!median {numbers}`""", inline=False)
            
            embed.add_field(name = "mode",value = """Calculates the mode (central tendency) of the given numeric or nominal data
                            Syntax: `!mod {numbers}`""", inline=False)
            
            embed.add_field(name = "StDev",value = """Calculates the standard deviation from a sample of data
                            Syntax: `!StDev {numbers}`""", inline=False)
            
            embed.add_field(name = "variance",value = """Calculates the variance from a sample of data
                            Syntax: `!variance {numbers}`""", inline=False)
            
            
            await ctx.send(embed = embed)
            

# * -------------------------------------------------------------------   
        
        else:
            embed = discord.Embed(
                title= "Invalid subcommand passed",
                description="Please provide a valid sub-command",
                color=discord.Color.red()
            )
            embed.set_author(name="Invalid", icon_url=ctx.author.display_avatar.url)
            
            await ctx.send(embed = embed)


# * -------------------------------------------------------------------   
# * -------------------------------------------------------------------   


async def setup(bot):
    await bot.add_cog(HelpCommand(bot))
        