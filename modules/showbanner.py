import random

class showbanner:
    def __init__(self):
        self.R="\033[0m\033[91m"
        self.B="\033[0m\033[94m"
        self.Y="\033[0m\033[93m"
        self.BY="\033[5m\033[93m"
        self.G="\033[0m\033[92m"
        self.Developer = f"\033[0m\033[1m{self.B}Developer {self.Y}: {self.G}HuiHola (Dhruv Namdev)\033[0m"
        self.GITHUB = f"\033[0m\033[1m{self.B}GitHub {self.Y}: {self.G}https://github.com/HuiHola\033[0m"
        self.WebSite = f"\033[0m\033[1m{self.B}Website {self.Y}: {self.G}https://huihola.github.io\033[0m"
        self.Telegram = f"\033[0m\033[1m{self.B}Telegram {self.Y}: {self.G}https://t.me/HuiHola\033[0m"
        self.Telegram_channel = f"\033[0m\033[1m{self.B}TGChannel {self.Y}: {self.G}https://t.me/shadowdiscussionworld\033[0m"

    def banner_one(self):
        print(f'''

        {self.BY}███   {self.Y}███                ███ {self.BY}  ███        
       {self.BY}███   {self.Y}███                ░░███{self.BY} ░░███       
      {self.BY}███   {self.Y}███      {self.B} ██████ {self.Y}    ░░███{self.BY} ░░███        
     {self.BY}░███  {self.Y}░███     {self.B} ███░░███  {self.Y}   ░███ {self.BY} ░███   
     {self.BY}░███  {self.Y}░███    {self.B} ░███ ░███  {self.Y}   ░███ {self.BY} ░███
     {self.BY}░░███ {self.Y}░░███   {self.B} ░███ ░███    {self.Y} ███  {self.BY} ███ 
      {self.BY}░░███ {self.Y}░░███  {self.B} ░░██████    {self.Y} ██░  {self.BY} ██░  
       {self.BY}░░░   {self.Y}░░░     {self.B}░░░░░░     {self.Y}░░░  {self.BY} ░░░                                               
                                            
  {self.R}                   ███ ███                {self.Developer}
  {self.R}                  ░███░███                {self.GITHUB}
  {self.R}                  ░███░███                {self.WebSite}
   {self.R}                 ░███░███                {self.Telegram}
     {self.R}               ░███░███                {self.Telegram_channel}
       {self.R}             ░███░███                
         {self.R}           ░███░███                
          {self.R}          ░░░ ░░░  

        ''')
    def banner_two(self):
        print(f'''

        {self.BY}███   {self.Y}███                ███ {self.BY}  ███        
       {self.BY}███   {self.Y}███                ░░███{self.BY} ░░███       
      {self.BY}███   {self.Y}███      {self.B} ██████ {self.Y}    ░░███{self.BY} ░░███        
     {self.BY}░███  {self.Y}░███     {self.B} ███  ███  {self.Y}   ░███ {self.BY} ░███   
     {self.BY}░███  {self.Y}░███    {self.B}  ███  ███  {self.Y}   ░███ {self.BY} ░███
     {self.BY}░░███ {self.Y}░░███   {self.B}  ███  ███    {self.Y} ███  {self.BY} ███ 
      {self.BY}░░███ {self.Y}░░███  {self.B}   ██████    {self.Y} ██░  {self.BY} ██░  
       {self.BY}░░░   {self.Y}░░░                {self.Y}░░░  {self.BY} ░░░                                               
                                            
  {self.R}                   ███ ███                {self.Developer}
  {self.R}                  ░███░███                {self.GITHUB}
  {self.R}                  ░███░███                {self.WebSite}
   {self.R}                 ░███░███                {self.Telegram}
     {self.R}               ░███░███                {self.Telegram_channel}
       {self.R}             ░███░███                
         {self.R}           ░███░███                
          {self.R}          ░░░ ░░░  

        ''')
    def showbanner(self):
        banner=random.randint(0,2)
        if(banner==0):
            self.banner_one()
        else:
            self.banner_two()
if __name__=="__main__":
    s=showbanner()
    s.showbanner()

