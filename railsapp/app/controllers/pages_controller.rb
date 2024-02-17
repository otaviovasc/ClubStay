class PagesController < ApplicationController
  skip_before_action :authenticate_user!, only: [ :home ]

  def home
    # Assuming you have scope or methods to filter customers and cards based on the parameters
    @customers = Customer.all
    @cards = Card.filter_by_params(params)
    respond_to do |format|
      format.html # For initial page load
      format.text { render partial: 'card_list', locals: { cards: @cards }, layout: false, formats: [:html] } # Assuming you have a _card_list.html.erb partial
    end
  end
end
