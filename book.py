class book:
  """Class to represent and store the details of a library book"""
  def __init__(self,book_id,title,author_name,position_number):
      """Constructor to initialize the fundamental attributes of a book."""
      self.book_id = book_id
      self.title=title
      self.author_name = author_name
      self.position_number = position_number
      self.is_available = True #The book is available when first added
  # Method 1: Check if the book is currently available
  def check_availability(self)
      """Checks and prints the current availability status of the book"""
    if self.is_available:
       print(f"'{self.title}'is available.")
    else:
        print(f"'{self.title}' is unavailable.")
      
 """Method 2 : updates the book status to unavailable if it is successfully borrowed"""
  def borrow_book(self,book_title):
    if self.is_avaialable== True:
       self.is_available = False #the text is taken,so it is not available from now
       return (f"'{self.book_title} is avaialable.please take it.")
    else:
       return f"sorry,'{self.book_title} is not available.")
      
  """Method 3:Updates the book status to avaialable if it is succesfully returned"""
  def return_book(self)
      self.is_available = True #Book is returned,so it is available now
      return (f"you have successfully returned'{self.book_title}| status:"avaialable now" ")
      
  ""Method 4:Displays the complete details and current status of the Book.""" 
   def get_status(self):
       print(f"Book ID":{self.book_id} | Title:{self.title}| Author:{self.author_name}")
            if self.is_available:
                 print("Status: Available")
            else:
                 print("Status: Unavaialable")


      
