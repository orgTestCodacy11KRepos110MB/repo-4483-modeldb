import * as React from 'react';
import { Link } from 'react-router-dom';
import { IRoute } from 'routes/makeRoute';
import routes from '../../routes';
import styles from './ProjectPageTabs.module.css';

interface ILocalProps {
  projectId: string;
  activeRoute: IRoute<any>;
}

export default class ProjectPageTabs extends React.Component<ILocalProps> {
  public render() {
    const { projectId, activeRoute } = this.props;

    return (
      <nav className={styles.nav_menu}>
        {this.renderActiveLink(
          routes.expirementRuns,
          { projectId },
          'Experiment Runs',
          activeRoute
        )}
        {this.renderActiveLink(
          routes.charts,
          { projectId },
          'Charts',
          activeRoute
        )}
      </nav>
    );
  }

  private renderActiveLink<T>(
    currentRoute: IRoute<T>,
    options: T,
    title: string,
    activeRoute: IRoute<T>
  ) {
    return (
      <Link
        className={currentRoute === activeRoute ? styles.active : ''}
        to={currentRoute.getRedirectPath(options)}
      >
        {title}
      </Link>
    );
  }
}
