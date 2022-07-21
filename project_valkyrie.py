# Application controller for Project Valkyrie aka DiscGO (dance, bag, throw, stats, etc.)
import DiscGO as dg
import DiscGOgui as dgg

# start application:
#   remove old pickle files (not needed, new onews will overwrite)
#   prepare data frame pickles
#       dg.make_pickles()
#           dg.make_pickle_mold_list()
#           dg.make_pickle_collection()
#   load data frame pickles - probably just as fast to pull from DB every time, but it's my program
#       dg.eat_pickle(filename)
# # SCREENS
#   main_window
#   mold_selection_window
#       df_mold_list
#   mold_comparison_matrix
#       df_filtered (pickle)
#   disc_collection_data
#       df_collection
#   disc_add_edit_form <--  app is waiting on this form
#       input: df_filtered + SQL lookup
#       output: SQL UPDATE / INSERT & COMMIT
#       dg.make_pickles()  # update data frames
#       dg.add_disc_to_collection(mold, options{})
#       dg.update_disc_in_collection(disc_id, options{})
#       dg.delete_disc_from_collection(disc_id)
#   bag_data (TBD, est. late July '22)
#   throw_data (TBD, est. late Aug '22)
#   category dashboards with charts & graphs (TBD)

if __name__ == '__main__':
    dg.make_dataframe_pickles()
    disc_list_df = dg.eat_pickle('mold_list.pkl').to_dict().items()
    print(f'DISC LIST: \n{disc_list_df}')
    dgg.run_window('main_window')